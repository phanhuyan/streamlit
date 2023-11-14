import streamlit as st

def create_columns(left_column_width=None, right_column_width=None):
  """Creates two columns in a Streamlit app.

  Args:
    left_column_width: The width of the left column, as a percentage of the total
      width. If None, the left column will be 50% wide.
    right_column_width: The width of the right column, as a percentage of the total
      width. If None, the right column will be 50% wide.

  Returns:
    A tuple of two Streamlit columns.
  """

  if left_column_width is None:
    left_column_width = 50
  if right_column_width is None:
    right_column_width = 50

  left_column, right_column = st.columns([left_column_width, right_column_width])

  # Make the left column scrollable.
  left_column.container(use_container_width=True)

  return left_column, right_column

import streamlit as st

def create_columns(left_column_width=None, right_column_width=None):
  """Creates two columns in a Streamlit app.

  Args:
    left_column_width: The width of the left column, as a percentage of the total
      width. If None, the left column will be 50% wide.
    right_column_width: The width of the right column, as a percentage of the total
      width. If None, the right column will be 50% wide.

  Returns:
    A tuple of two Streamlit columns.
  """

  if left_column_width is None:
    left_column_width = 50
  if right_column_width is None:
    right_column_width = 50

  left_column, right_column = st.columns([left_column_width, right_column_width])

  # Make the left column scrollable.
  left_column.container(use_container_width=True)

  return left_column, right_column

if __name__ == '__main__':

  left_column, right_column = create_columns()

  # Add content to the left column.
  left_column.header('Scrollable Column')
  for i in range(100):
    left_column.write(f'Item {i}')

  # Add content to the right column.
  right_column.header('Static Column')
  right_column.write('This column is static.')
