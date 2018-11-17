
# DOGS_PER_PACK =10 
# BUNS_PER_PACK = 8

# guest_count = int(input( ' Enter the number of people: '))
# hotdogs_per_guest = int(input( ' Enter the number of hotdogs: '))

# hotdogs_eaten = guest_count*hotdogs_per_guest

# dog_pack_count = hotdogs_eaten //DOGS_PER_PACK

# if dog_pack_count * BUNS_PER_PACK <hotdogs_eaten:
#   dog_pack_count += 1
#   dogs_uneaten_count = dog_pack_count * DOGS_PER_PACK - hotdogs_eaten
  
  


# print('hotdog bun count', bun_package_count)
# print('hotdogs uneaten', dogs_uneaten_count)
# print('hotdog package count', dog_pack_count)

HOTDOGS_PER_PACK =10 
HOTDOG_BUNS_PER_PACK = 8

number_of_guest = int(input( ' Enter the number of people: '))
hotdogs_per_guest = int(input( ' Enter the number of hotdogs: '))

hotdogs_eaten = number_of_guest*hotdogs_per_guest

hotdog_packs_used = hotdogs_eaten//HOTDOGS_PER_PACK+1

hotdog_bun_packs_used = (hotdogs_eaten//HOTDOG_BUNS_PER_PACK)+(hotdogs_eaten%HOTDOG_BUNS_PER_PACK>0)

hotdogs_left = (HOTDOGS_PER_PACK*hotdog_packs_used)-(hotdogs_eaten)

hotdog_buns_left =  (HOTDOG_BUNS_PER_PACK*hotdog_bun_packs_used)-(hotdogs_eaten)


# hotdogs_left_over =

# hotdog_buns_left_over =

print('The number packs hotdogs required: ',hotdog_packs_used)
print('The number of hotdog bun packs required: ',hotdog_bun_packs_used)
print('The number of left over hotdogs: ',hotdogs_left)
print('The number of left over hotdog buns: ',hotdog_buns_left)
#min hotdog packs required 
#min hotdog bun packs required 
#left over hotdogs 
#left over buns


