from bs4 import BeautifulSoup
import nltk
import re

class HtmlContactExceptino(Exception):
    pass

class HtmlContact(object):


    email_regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                            "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                            "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

    def __init__(self, html, target_contacts=None):
        self.target_contacts = target_contacts
        self.html = html
        self.soup = None

    def search(self):
        # Searches the html in question
        if self.soup == None:
            self.soup = BeautifulSoup(self.html,'html.parser')
        self.emails  = list(set(self.get_emails(self.html))) #TODO search email here

    def search_target_contacts(self):
        # returns the initial target_contacts that we initialized with, but with their contact info hopefully filled.
        self.search()
        for target_contact in self.target_contacts:
            target_contact.email =  self.best_email_for_contact(target_contact)

    def best_email_for_contact(self, target_contact):
        email_scores = [(self.score_token(email, first_name=target_contact.first_name, last_name=target_contact.last_name), email) for email in self.emails]
        #match each email to the target_contact, pick the one with the lowest nltk distance
        sorted_scores = sorted(email_scores, key=lambda tup: tup[0]) #small to big, meaning smallest to largest
        if len(sorted_scores) == 0:
            return ""
        else:
            return sorted_scores[0][1]

    def score_token(self, email, first_name="", last_name="", bias=0.0):
        # Returns a score for the likeliyhood that the token belongs to the name.
        # Lower is better
        return min(nltk.metrics.edit_distance(email, last_name.lower()),
            nltk.metrics.edit_distance(email, first_name.lower())) + bias

    def get_emails(self, s):
        '''
        @author dideler@github
        Returns an iterator of matched emails found in string s.
        '''
        # Removing lines that start with '//' because the regular expression
        # mistakenly matches patterns like 'http://foo@bar.com' as '//foo@bar.com'.
        return ([email[0] for email in re.findall(self.email_regex, s) if not email[0].startswith('//')])

class Contact(object):
    '''
    This class represents an individual Contact
    '''

    def __init__(self, first_name="", last_name="", email=""):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def update_with_contact(contact):
        pass
