import argparse
from config import Session
from models import Group, Student, Teacher, Subject
from sqlalchemy.orm import Session as SessionType

def create_entity(session: SessionType, model, args):
    entity = model()
    for key, value in vars(args).items():
        if hasattr(entity, key) and value is not None:
            setattr(entity, key, value)
    session.add(entity)
    session.commit()
    print(f"{model.__name__} created with id {entity.id}")

def list_entities(session: SessionType, model):
    items = session.query(model).all()
    for item in items:
        print(item.__dict__)

def update_entity(session: SessionType, model, args):
    entity = session.get(model, args.id)
    if not entity:
        print(f"{model.__name__} with id {args.id} not found")
        return
    for key, value in vars(args).items():
        if hasattr(entity, key) and value is not None and key != 'id':
            setattr(entity, key, value)
    session.commit()
    print(f"{model.__name__} with id {args.id} updated")

def remove_entity(session: SessionType, model, args):
    entity = session.get(model, args.id)
    if not entity:
        print(f"{model.__name__} with id {args.id} not found")
        return
    session.delete(entity)
    session.commit()
    print(f"{model.__name__} with id {args.id} removed")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', '-a', choices=['create', 'list', 'update', 'remove'], required=True)
    parser.add_argument('--model', '-m', choices=['Group', 'Student', 'Teacher', 'Subject'], required=True)
    parser.add_argument('--id', type=int)
    parser.add_argument('--name', '-n')

    args = parser.parse_args()

    model_map = {
        'Group': Group,
        'Student': Student,
        'Teacher': Teacher,
        'Subject': Subject
    }

    model = model_map[args.model]

    with Session() as session:
        if args.action == 'create':
            create_entity(session, model, args)
        elif args.action == 'list':
            list_entities(session, model)
        elif args.action == 'update':
            if args.id is None:
                print("ID is required for update")
                return
            update_entity(session, model, args)
        elif args.action == 'remove':
            if args.id is None:
                print("ID is required for remove")
                return
            remove_entity(session, model, args)

if __name__ == '__main__':
    main()
