mycursor.execute("Update shows set seats_left=(seats_left-1) where showId=%s;",(currentShow))
        # db.commit()