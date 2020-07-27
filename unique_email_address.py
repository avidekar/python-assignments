# Every
# email
# consists
# of
# a
# local
# name and a
# domain
# name, separated
# by
# the @ sign.
#
# For
# example, in alice @ leetcode.com, alice is the
# local
# name, and leetcode.com is the
# domain
# name.
#
# Besides
# lowercase
# letters, these
# emails
# may
# contain
# '.'
# s or '+'
# s.
#
# If
# you
# add
# periods('.')
# between
# some
# characters in the
# local
# name
# part
# of
# an
# email
# address, mail
# sent
# there
# will
# be
# forwarded
# to
# the
# same
# address
# without
# dots in the
# local
# name.For
# example, "alice.z@leetcode.com" and "alicez@leetcode.com"
# forward
# to
# the
# same
# email
# address.(Note
# that
# this
# rule
# does
# not apply
# for domain names.)
#
# If
# you
# add
# a
# plus('+') in the
# local
# name, everything
# after
# the
# first
# plus
# sign
# will
# be
# ignored.This
# allows
# certain
# emails
# to
# be
# filtered,
# for example m.y + name @ email.com will be forwarded to my @ email.com.(Again, this rule does not apply for domain names.)
#
# It is possible
# to
# use
# both
# of
# these
# rules
# at
# the
# same
# time.
#
# Given
# a
# list
# of
# emails, we
# send
# one
# email
# to
# each
# address in the
# list.How
# many
# different
# addresses
# actually
# receive
# mails?
#
# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails

def find_unique_email_ids(emails):

    email_set = set()
    for email in emails:
        email_id = email.split("@")
        email_id[0] = email_id[0].split("+")[0].replace(".","")
        email = "@".join(email_id)
        if email not in email_set:
            email_set.add(email)

    print(len(email_set))

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com"]

find_unique_email_ids(emails)