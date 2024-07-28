import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def process_pokemon_file(json_file):
    # Read the contents of the json file.
    async with aiofiles.open(json_file, mode='r') as f:
        contents = await f.read()
    
    # Load it into a dictionary and create a list of moves.
    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]

    # Open a new file to write the list of moves into.
    async with aiofiles.open(f'{pokemonmove_directory}/{name}_move.txt', mode='w') as f:
        await f.write('\n'.join(moves))

async def main():
    # Get the list of JSON files in the directory.
    json_list = Path(pokemonapi_directory).glob('*.json')

    # Create a list of tasks to process each file.
    tasks = [process_pokemon_file(json_file) for json_file in json_list]

    # Run the tasks concurrently.
    await asyncio.gather(*tasks)

asyncio.run(main())

