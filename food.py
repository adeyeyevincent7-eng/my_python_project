foods_you_like = {"jollof rice", "plantain", "suya", "egusi soup", "puff-puff"}
foods_your_friend_likes = {"jollof rice", "fried rice", "suya", "moi moi", "plantain"}
foods_available_at_canteen = {"jollof rice", "beans", "plantain", "suya", "spaghetti"}

# Foods both you and your friend like
both_like = foods_you_like & foods_your_friend_likes
print("Both like:", both_like)

# Foods only you like
only_you = foods_you_like - foods_your_friend_likes
print("Only you like:", only_you)

# Foods both of you like that are also available at the canteen
both_and_available = (foods_you_like & foods_your_friend_likes) & foods_available_at_canteen
print("Both like & available at canteen:", both_and_available)