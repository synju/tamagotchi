from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize Tamagotchi instance globally
tamagotchi_instance = None  # This will hold the reference to the Tamagotchi instance


class TamagotchiAPI:
	def __init__(self, tamagotchi):
		global tamagotchi_instance
		tamagotchi_instance = tamagotchi  # Assign the Tamagotchi instance to global

	def start_api(self):
		app.run(host='0.0.0.0', port=5000)


@app.route('/status', methods=['GET'])
def get_status():
	global tamagotchi_instance
	if tamagotchi_instance:
		status = {'name': tamagotchi_instance.name, 'health': tamagotchi_instance.health, 'hunger': tamagotchi_instance.hunger, 'happiness': tamagotchi_instance.happiness, 'hygiene': tamagotchi_instance.hygiene, 'age': tamagotchi_instance.age, 'sleeping': tamagotchi_instance.sleeping}
		return jsonify(status)
	else:
		return jsonify({"error": "Tamagotchi instance not found"}), 500


@app.route('/action', methods=['POST'])
def perform_action():
	global tamagotchi_instance
	data = request.json
	action = data.get('action', None)

	if tamagotchi_instance and action:
		if action == 'feed':
			tamagotchi_instance.feed()
		elif action == 'clean':
			tamagotchi_instance.clean()
		elif action == 'play':
			tamagotchi_instance.play()
		elif action == 'medicine':  # Added medicine action
			tamagotchi_instance.give_medicine()
		return jsonify({'message': f'Action {action} performed'})
	return jsonify({'message': 'Invalid action'}), 400
