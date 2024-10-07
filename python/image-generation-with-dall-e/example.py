from openai import OpenAI

OpenAI.api_key = 'OpenAI API Key'
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="A mesmerizing, fairytale-style moonlit forest, bathed in the soft glow of a small moon shining in a beautifully starry night sky. At the center, a winding, realistic forest path made of uneven, naturally worn pebbles leads deep into the heart of the forest. The road curves and meanders gently, blending into the landscape as though shaped by countless footsteps over time. Its edges are slightly overgrown with moss and roots, following the natural contours of the forest with subtle bends and turns, giving the trail an authentic, aged look. Both sides of the path are lined with an abundance of colorful, translucent magical flowers and glowing mushrooms, their light casting soft hues over the scene. Countless fireflies hover gently, adding a dreamy sparkle to the surroundings. The atmosphere is serene and enchanting, with a smooth, lifelike blend of light and shadow that enhances the forest’s magical realism. Make the scene smoother and more realistic.",
  size="1792x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
