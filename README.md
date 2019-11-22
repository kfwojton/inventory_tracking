# inventory_tracking

staging server --> https://inventorytrackerk.herokuapp.com/


Sample .env

# General Guidelines 

This is a demo MVP app to show a potential data architecture for inventory tracking site. 

```
# Only needed for testing email sends, for this to work you need enable allow insecure apps on said gmail account

EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

SECRET_KEY=2gApQrwNlqtE/DQ2GDTPqXUESc2r1/Ft0uJ0D+8t


# LOCAL ENV #
#############

# DATABASE_NAME=kevinwojton
# DATABASE_USER=kevinwojton
# DATABASE_PASSWORD=
# DATABASE_HOST=localhost
# DATABASE_PORT=



# STAGING ENV #
###############

DATABASE_NAME=d3tq2qmga3vu7d
DATABASE_USER=nhjmfrwcoenicf
DATABASE_PASSWORD=f72fb23299783eb9b7d0e3864a8b21502f23f71c04b787ae566a6b727441e2b1
DATABASE_HOST=ec2-107-20-244-40.compute-1.amazonaws.com
DATABASE_PORT=5432
SERVER_NAME=staging
AWS_ACCESS_KEY_ID=AKIARBVACZNZW7A6VIXX
AWS_SECRET_ACCESS_KEY=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
AWS_STORAGE_BUCKET_NAME=booya-static


# PRODUCTION ENV #
##################

# DATABASE_NAME=dcfm6b26d0n2s6
# DATABASE_USER=yinpbcgsvhucnt
# DATABASE_PASSWORD=5f998df3f799f0c02617bd60a5b11bbf55cbfb5ac9adb82ab321b0a1f5d1c764
# DATABASE_HOST=ec2-50-19-254-63.compute-1.amazonaws.com
# DATABASE_PORT=5432
```
