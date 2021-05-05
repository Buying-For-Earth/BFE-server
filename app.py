from app import app
import os

port = int(os.environ.get("PORT", 8000))
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=port)