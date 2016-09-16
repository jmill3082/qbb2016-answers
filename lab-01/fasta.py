
"""
Parse every FASTA record from stdin and print each.
"""

class FASTAReader( object ):
    def __init__( self , file ):
        self.file = file
        self.last_id = None
        self.inc = 0
    
    def __iter__( self ):
        return self
        
    def next( self ):
        if self.last_id is None:        
            line = self.file.readline()
            if line == "":
                raise StopIteration 
            # Verify this is a header line
            # assert line.startswith( ">" )

            # Extract the id - whole line
            # identifier = line[1:].rstrip( "\r\n" )
            #   OR
            # Extract the id - just the first part of the id
            identifier = line[1:].split()[0]
        else:
            identifier = self.last_id
            
        sequences = []

        while 1:
            line = self.file.readline().rstrip( "\r\n" )
            if line.startswith( ">" ):
                self.last_id = line[1:].split()[0]
                # print "new header", self.inc
                self.inc += 1
                break
            elif line == "":
                if sequences:
                    return identifier, "".join( sequences )
                ## return None, None
                # print "stop iter"
                raise StopIteration
            else:
                sequences.append( line )
        

        return identifier, "".join( sequences )
