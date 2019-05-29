LDAP Server URI
    ldap://windows.cloud.lab:389
LDAP Bind DN
    CN=Administrator,CN=Users,DC=cloud,DC=lab
LDAP Group Type
    ActiveDirectoryGroupType
LDAP Require Group
    CN=Tower_Users,CN=Users,DC=cloud,DC=lab
LDAP User Search
[
 "DC=cloud,DC=lab",
 "SCOPE_SUBTREE",
 "(sAMAccountName=%(user)s)"
]
LDAP Group Search
[
 "DC=cloud,DC=lab",
 "SCOPE_SUBTREE",
 "(objectClass=group)"
]
LDAP User Attribution Map
{
 "first_name": "givenName",
 "last_name": "sn",
 "email": "mail"
}
