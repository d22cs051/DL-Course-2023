from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = ''
    settings.got10k_path = '/DATA1/bikash_dutta/DL/Major/data/got10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.lasot_extension_subset_path = ''
    settings.lasot_lmdb_path = ''
    settings.lasot_path = ''
    settings.network_path = '/DATA1/bikash_dutta/DL/Major/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/DATA1/bikash_dutta/DL/Major/data/nfs'
    settings.otb_path = '/DATA1/bikash_dutta/DL/Major/data/OTB2015'
    settings.prj_dir = '/DATA1/bikash_dutta/DL/Major'
    settings.result_plot_path = '/DATA1/bikash_dutta/DL/Major/test/result_plots'
    settings.results_path = '/DATA1/bikash_dutta/DL/Major/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/DATA1/bikash_dutta/DL/Major'
    settings.segmentation_path = '/DATA1/bikash_dutta/DL/Major/test/segmentation_results'
    settings.tc128_path = '/DATA1/bikash_dutta/DL/Major/data/TC128'
    settings.tn_packed_results_path = ''
    settings.tnl2k_path = '/DATA1/bikash_dutta/DL/Major/data/tnl2k'
    settings.tpl_path = ''
    settings.trackingnet_path = '/DATA1/bikash_dutta/DL/Major/data/trackingnet'
    settings.uav_path = '/DATA1/bikash_dutta/DL/Major/data/UAV123'
    settings.vot_path = '/DATA1/bikash_dutta/DL/Major/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

