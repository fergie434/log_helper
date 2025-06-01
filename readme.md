# log_helper


## Installation

```bash
pip3 install git+https://github.com/fergie434/log_helper
```

## Usage

### Set up a logger object with default settings

```python
logger = log_helper.setup_logging('proxmox_monitor.log')
```
#### The default settings are 
```
log_filename='log.log'      # Name for the log file
log_maxbytes=4000000        # Max size of each log file before rolling
log_filecount=5             # Number of files to keep
log_directory='logs'        # Parent directory for logs to be stored (This folder will be created automatically)
```
### Set up a logger object with custom settings:
```python
logger = log_helper.setup_logging(log_filename='mylogname.log', log_maxbytes=1234560, log_filecount=5, log_directory='logs')
logger.info('Script Starting')
```

### Write to log at info level
```python
logger = log_helper.setup_logging('proxmox_monitor.log')
logger.info('Script Starting')
```
