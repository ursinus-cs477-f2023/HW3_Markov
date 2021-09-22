class MarkovModel:
    def __init__(self, k):
        """
        Initialize a Markov model with a particular prefix length
        
        Parameters
        ----------
        k: int
            Length of prefix to use
        """
        self.k = k
        ## TODO: Setup any other member variables that might be useful
    
    def load_file(self, filename):
        """
        Load in an entire file as one string and add
        it to the model

        Parameters
        ----------
        filename: string
            Path to file to load
        """
        fin = open(filename)
        self.add_string(fin.read())
        fin.close()
    
    def load_file_lines(self, filename):
        """
        Load in an entire file as one string and add
        it to the model

        Parameters
        ----------
        filename: string
            Path to file to load
        """
        fin = open(filename)
        for line in fin.readlines():
            line = line.rstrip()
            if len(line) > 0:
                # Add space after period to help with transitions
                if line[-1] == ".": 
                    line += " "
                self.add_string(line)
        fin.close()
    
    def add_string(self, s):
        """
        Incorporate a particular string into your model by adding any prefixes
        if they don't exist and by updating counts
        """
        ## TODO: Fill this in
        return # This does nothing
    
    def get_log_probability(self, s):
        """
        Compute the log probability of a particular string according to the model

        Parameters
        ----------
        s: string
            String for which to compute the probability
        
        Returns
        -------
        float: Log probability
        """
        ## TODO: Fill this in
        return 0 # This is a dummy value

    def synthesize_text(self, length):
        """
        Synthesize random text of a particular length in the style captured
        by this model

        Parameters
        ----------
        length: int
            How many characters are in the string to synthesize
        
        Returns
        -------
        string: The synthesized text
        """
        ## TODO: Fill this in
        return "" # This does nothing