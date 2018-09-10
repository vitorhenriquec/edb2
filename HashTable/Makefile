## Makefile template created by João Pedro de Amorim Paula
#  Edited by Vitor Henrique Coelho Bezerra

SHELL = /bin/sh

# Define here the directories you'll use in your project.
INCDIR = ./include
SRCDIR = ./src
OBJDIR = ./build
BINDIR = ./bin

# Define here some variables (or macros) that you'll tons of times.
CC = g++
CFLAGS = -O0 -Wall -Wextra -ansi -pedantic -g -ggdb -std=c++11 -lm -I. -I$(INCDIR)
RM = rm
OBJS = $(addprefix $(OBJDIR)/,hashtable.o)
# Here on the OBJS I look for the files specified inside the (addprefix) and
# after the comma and add the $(OBJDIR) is added to the beginning of each of the
# files. More info on (https://www.gnu.org/software/make/manual/html_node/File-Name-Functions.html).

# Phony targets (for more information, visit https://www.gnu.org/software/make/manual/make.html#Phony-Targets)
.PHONY: clean cleanobj cleanbin
.PHONY: all main build
.PHONY: hashtable

# Use "make" to execute everything
all: main

# Use "make main" to compile the main
main: $(BINDIR)/programa

# Compiles the main
$(BINDIR)/programa: $(SRCDIR)/main.cpp $(INCDIR)/hashtable.hpp
	mkdir -p $(BINDIR)
	$(CC) $(CFLAGS) $^ -o $@

# Removes all objects
cleanobj:
	$(RM) $(OBJDIR)/*.o

# Removes all executables
cleanbin:
	$(RM) $(BINDIR)/*

# Removes all executables and all objects
clean: cleanobj cleanbin
