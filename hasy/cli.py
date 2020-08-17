# Core Library modules
import logging
import sys

# First party modules
from hasy.hasy_tools import (
    _analyze_class_distribution,
    _analyze_cm,
    _analyze_correlation,
    _analyze_distances,
    _analyze_pca,
    _analyze_variance,
    _count_users,
    _create_stratified_split,
    _create_verification_task,
    _get_color_statistics,
    _load_csv,
    _verify_all,
    create_random_overview,
)

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
    stream=sys.stdout,
)


def _get_parser():
    """Get parser object for hasy_tools.py."""
    # Core Library modules
    import argparse
    from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

    parser = ArgumentParser(
        description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--dataset", dest="dataset", help="specify which data to use")
    parser.add_argument(
        "--verify",
        dest="verify",
        action="store_true",
        default=False,
        help="verify PNG files",
    )
    parser.add_argument(
        "--overview",
        dest="overview",
        action="store_true",
        default=False,
        help="Get overview of data",
    )
    parser.add_argument(
        "--analyze_color",
        dest="analyze_color",
        action="store_true",
        default=False,
        help="Analyze the color distribution",
    )
    parser.add_argument(
        "--class_distribution",
        dest="class_distribution",
        action="store_true",
        default=False,
        help="Analyze the class distribution",
    )
    parser.add_argument(
        "--distances",
        dest="distances",
        action="store_true",
        default=False,
        help="Analyze the euclidean distance distribution",
    )
    parser.add_argument(
        "--pca",
        dest="pca",
        action="store_true",
        default=False,
        help=(
            "Show how many principal components explain "
            "90%% / 95%% / 99%% of the variance"
        ),
    )
    parser.add_argument(
        "--variance",
        dest="variance",
        action="store_true",
        default=False,
        help="Analyze the variance of features",
    )
    parser.add_argument(
        "--correlation",
        dest="correlation",
        action="store_true",
        default=False,
        help="Analyze the correlation of features",
    )
    parser.add_argument(
        "--create-classification-task",
        dest="create_folds",
        action="store_true",
        default=False,
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--create-verification-task",
        dest="create_verification_task",
        action="store_true",
        default=False,
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--count-users",
        dest="count_users",
        action="store_true",
        default=False,
        help="Count how many different users have created the dataset",
    )
    parser.add_argument(
        "--analyze-cm",
        dest="cm",
        default=False,
        help="Analyze a confusion matrix in JSON format.",
    )
    return parser


def entry_point():
    args = _get_parser().parse_args()
    if args.verify:
        if args.dataset is None:
            logging.error("--dataset needs to be set for --verify")
            sys.exit()
        _verify_all(args.dataset)
    if args.overview:
        img_src = _load_csv(args.dataset)
        create_random_overview(img_src, x_images=10, y_images=10)
    if args.analyze_color:
        _get_color_statistics(csv_filepath=args.dataset)
    if args.class_distribution:
        _analyze_class_distribution(
            csv_filepath=args.dataset, max_data=1000, bin_size=25
        )
    if args.pca:
        _analyze_pca(csv_filepath=args.dataset)
    if args.distances:
        _analyze_distances(csv_filepath=args.dataset)
    if args.variance:
        _analyze_variance(csv_filepath=args.dataset)
    if args.correlation:
        _analyze_correlation(csv_filepath=args.dataset)
    if args.create_folds:
        _create_stratified_split(args.dataset, int(args.create_folds))
    if args.count_users:
        _count_users(csv_filepath=args.dataset)
    if args.create_verification_task:
        _create_verification_task()
    if args.cm:
        _analyze_cm(args.cm)


if __name__ == "__main__":
    entry_point()
