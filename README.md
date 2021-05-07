## Introduction

gitsync is a tool to sync git repo to plastic

## Getting Start

### image build


```
cd <gitsync_dir>
docker build -t $IMAGE_NAME .
```
for example:
```
docker build -t gitsync .
```
### image run

```
docker run -v <YOUR_DATA_FOLDER>:<TARGET_DATA_FOLDER> $IMAGE_NAME
```
for example:
```
docker run -v /Users/unity/Documents/GitHub/gitsync/data:/gitSync/data gitsync
```