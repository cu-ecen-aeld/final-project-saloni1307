CROSS_COMPILE=

ifeq ($(CC),)
	CC=$(CROSS_COMPILE)gcc
endif

ifeq ($(CFLAGS),)
	CFLAGS= -g -Wall -Werror
endif

all: client server
default: client server

client : client.o
	$(CROSS_COMPILE)$(CC) $(CFLAGS) -o client client.o

server : server.o
	$(CROSS_COMPILE)$(CC) $(CFLAGS) -o server server.o

client.o: client.c
	$(CROSS_COMPILE)$(CC) $(CFLAGS) -c client.c

server.o: server.c
	$(CROSS_COMPILE)$(CC) $(CFLAGS) -c server.c

clean :
	rm -f client server *.o