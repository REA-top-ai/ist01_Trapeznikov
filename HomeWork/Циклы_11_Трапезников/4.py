dog_breeds_available_for_adoption =  ['french bulldog', 'dalmatian',
                                      'shih-tzu', 'poodle', 'collie']
dog_breed_i_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
    print(dog)
    if dog == dog_breed_i_want:
        print("У них есть собака, которую я хочу!")
        break