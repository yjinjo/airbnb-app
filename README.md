# Airbnb API
## Instruction
### Start Project
```bash
git clone https://github.com/yjinjo/airbnb-app --branch blueprint --single-branch [Your Directory]
```

```bash
poetry install
```

Make .env file and put `SETTINGS_SECRET_KEY` in there. 

For example, 
```bash
SETTINGS_SERECT_KEY="adsfklqnwlkgwiperwn23iu89234njk" 
```

```bash
python manage.py mega_seed
```
This command creates 20 random users, 150 rooms, and 31 photos in uploads/room_photos. 
You can check in core/management/commands/mega_seed.py

