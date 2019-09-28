from django.core.mail import EmailMessage


class EmailSAMessage(EmailMessage):

    def __init__(self, subject='', body='', from_email=None, to=None, bcc=None,
                 connection=None, attachments=None, headers=None, reply_to=None):
        """
        Initialize a single email message whose properties can be set and get externally,
        With verification in built for its properties.
        """
        super().__init__(
            subject, body, from_email, to, bcc, connection, attachments,
            headers, reply_to,
        )

    # using property decorator 
    # a getter function 
    @property
    def subject(self): 
        return self.subject
    
    # a setter function 
    @subject.setter 
    def subject(self, subj): 
        self.subject = subj

    # using property decorator 
    # a getter function 
    @property
    def body (self): 
        return self.body 
    
    # a setter function 
    @body.setter 
    def body(self, b): 
        self._body = b

    # using property decorator 
    # a getter function 
    @property
    def to (self): 
        return self.to 
    
    # a setter function 
    @to.setter 
    def to(self, t): 
        self.to = t

    # using property decorator 
    # a getter function 
    @property
    def from_email (self): 
        return self.from_email
    
    # a setter function 
    @from_email.setter 
    def from_email(self, f_e): 
        self.to = f_e

    # using property decorator 
    # a getter function 
    @property
    def bcc (self): 
        return self.bcc
    
    # a setter function 
    @bcc.setter 
    def bcc(self, b_c): 
        self.bcc = b_c

    # using property decorator 
    # a getter function 
    @property
    def connection (self): 
        return self.connection
    
    # a setter function 
    @connection.setter 
    def connection(self, con): 
        self.connection = con

    # using property decorator 
    # a getter function 
    @property
    def attachments (self): 
        return self.attachments
    
    # a setter function 
    @attachments.setter 
    def attachments(self, attach): 
        self.attachments = attach

    # using property decorator 
    # a getter function 
    @property
    def headers (self): 
        return self.attachments
    
    # a setter function 
    @headers.setter 
    def headers(self, head): 
        self.headers = head

    # using property decorator 
    # a getter function 
    @property
    def reply_to (self): 
        return self.attachments
    
    # a setter function 
    @reply_to.setter 
    def reply_to(self, rep_to): 
        self.reply_to = rep_to

