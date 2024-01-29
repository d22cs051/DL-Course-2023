from TrackingNet.Downloader import TrackingNetDownloader
from TrackingNet.utils import getListSplit


downloader = TrackingNetDownloader(LocalDirectory="data/TrackingNet1")

for split in getListSplit():
    downloader.downloadSplit(split)