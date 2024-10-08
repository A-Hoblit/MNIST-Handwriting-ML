CC=g++
INCLUDE_DIR := $(ROOT)/include
SRC := $(ROOT)/src
CFLAGS += -shared -std=c++11 -g
LIB_DATA := libdata.so

all: $(LIB_DATA)

