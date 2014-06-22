import os
import sqlite3
import optparse


def printTables(iphoneDb):
    try:
        conn = sqlite3.connect(iphoneDb)
        c = conn.cursor()
        c.execute('SELECT tbl_name FROM sqlite_master \
        WHERE type==\"table\":')
        print "\n[*] Database: " + iphoneDb
        for row in c:
            print "[-] Table: " + str(row)
    except:
        pass
    conn.close()
    
    
def isMessageTable(iphoneDb):
    try:
        conn = sqlite3.connect(iphoneDb)
        c = conn.cursor()
        c.execute('SELECT tbl_name FROM sqlite_master \
        WHERE type==\"table\":')
        for row in c:
            if 'message' in str(row):
                return True
    except:
        return False
    
 
def printMessage(msgDb):
    try:
        conn = sqlite3.connect(msgDb)
        c = conn.cursor()
        c.execture('select datetime(date, \'unixepock\'),\
        address, text from message WHERE address>0:')
        for row in c:
            date = str(row[0])
            addr = str(row[1])
            text = row[2]
            print '\n[+] Date: ' + date + ', Addr: '+addr \
            + ' Message: ' + text
    except:
        pass
    
       
def main():
    parser = optparse.OptionParser("usage%prog " +\
                                   "-p <iPhone Backup Directory> ")
    parser.add_option('-p', dest='pathName',\
                      type='string', help='specify iPhone Backup Directory')
    (options, args) = parser.parse_args()
    pathName = options.pathName
    if pathName == None:
        print parser.usage
        exit(0)
    else:
        dirList = os.listdir(pathName)
        for fileName in dirList:
            iphoneDb = os.path.join(pathName, fileName)
            if isMessageTable(iphoneDb):
                try:
                    print '\n[*] --- Found Messages ---'
                    printMessage(iphoneDb)
                except:
                    pass
                
if __name__ == '__main__':
    main()