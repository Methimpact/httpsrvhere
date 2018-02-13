#!/usr/bin/env python
"""
mth_py_httpsrvhere: Simple HTTP server to serv local dir
v: 1.0.2
d: 06022018
"""
import sys, os
import time
import optparse
import SimpleHTTPServer
import SocketServer

MKVRSN = "1.0.2_06022018"
MKPROG = "httpsrvhere"
MKDESC = "meka_py_httpsrvhere: Simple HTTP server to serv local dir"
MKEPIL = "a meka nekal creation with <3"

PORT = 38080
ADDR = "0.0.0.0"

SMPLSRVR_EXT = { '.webapp': 'application/x-web-app-manifest+json', }

def prs_cmdline(  ):
    prog        = MKPROG
    version     = "%prog " + MKVRSN
    description = MKDESC
    epilog      = MKEPIL
    o = optparse.OptionParser(prog=prog, version=version, description=description, epilog=epilog )
    o.add_option( "-p", "--port",    dest="LPORT",      help="Listen Port,\tdef:%d"%PORT,       default=PORT, type=int ) #action="store_true", default=False)
    o.add_option( "-l",              dest="LADDR",      help="Listen Address,\tdef:%s"%ADDR,    default=ADDR, type=str )
    #o.add_option("-f",dest="logfn",help="File to save logs",default="/var/log/httpsrvhere" )
    return o.parse_args()

def bld_url( sa, lurl = "http://" ):
    if sa[0]=="" or sa[0]=="0.0.0.0":                       lurl+="127.0.0.1"
    else:                                                   lurl+=sa[0]
    if sa[1]!=80:                                           lurl+=":%d"%sa[1]
    lurl+="/"
    return lurl

def prep_server(options):
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    Handler.extensions_map.update(SMPLSRVR_EXT)
    httpd = SocketServer.TCPServer((options.LADDR, options.LPORT),Handler)
    return Handler, httpd

def main( ):
    options, args = prs_cmdline()
    lurl = "http://"
    print( "[!] Server INIT..." )
    Handler, httpd = prep_server( options )
    print( "[!] Server STARTING !" )
    lurl = bld_url( httpd.socket.getsockname( ) )
    print( "[+] Serving at port %s:%d" % ( options.LADDR, options.LPORT ) )
    print( " \\__ %s" % lurl )
    httpd.serve_forever( )

if __name__ == '__main__':
    main( )
