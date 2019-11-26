import os

default_user = os.environ["USER"]
file_count_reprint_no = 15
DPM = "://se01.dur.scotgrid.ac.uk/dpm/dur.scotgrid.ac.uk/home/pheno/{0}/"
## possible protocols:
## recommended:
# gsiftp, srm (slow, but reliable), dav, davs, xroot
## less reliable protocols:
# root, https, s3, lfc, guid, rfio, dcap
## not supported by gfal:
# sftp, mock
protocol_default = "gsiftp"
protocol_list = "davs"
protocol_delete = "xroot"
protocol_download = "xroot"
protocol_upload = "xroot"
protocol_move = "xroot"
protocol_mkdir = "srm"
dir_colour = 33
exe_colour = 34
use_fnmatch = False
