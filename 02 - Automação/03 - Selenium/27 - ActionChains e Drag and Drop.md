# ActionChains e Drang and Drop


```python
from selenium.webdriver import ActionChains


# Localize o elemento que deseja arrastar
element_to_drag = driver.find_element_by_id('element-to-drag')

# Localize o elemento onde deseja soltar
drop_target = driver.find_element_by_id('drop-target')

# Crie uma instância de ActionChains
chain = ActionChains(driver)

# Execute o "drag and drop"
chain.drag_and_drop(element_to_drag, drop_target).perform()
```