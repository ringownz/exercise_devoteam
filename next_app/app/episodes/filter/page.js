// filter episodes by rating and by season
"use client"

import {Dropdown, DropdownTrigger, DropdownMenu, DropdownItem, Button} from "@nextui-org/react";

export default function App() {

  return (
    <div className="center"> 
      <Dropdown>
        <DropdownTrigger>
          <Button 
            variant="bordered" 
          >
            Open Menu
          </Button>
        </DropdownTrigger>
        <DropdownMenu 
          aria-label="Link Actions" 
          onAction={(key) => updateData(key)}
        >
          <DropdownItem key="0" href="/episodes/filter/0">All</DropdownItem>
          <DropdownItem key="1" href="/episodes/filter/1">1</DropdownItem>
          <DropdownItem key="2" href="/episodes/filter/2">2</DropdownItem>
          <DropdownItem key="3" href="/episodes/filter/3">3</DropdownItem>
          <DropdownItem key="4" href="/episodes/filter/4">4 </DropdownItem>
          <DropdownItem key="5" href="/episodes/filter/5">5</DropdownItem>
          <DropdownItem key="6" href="/episodes/filter/6">6</DropdownItem>
          <DropdownItem key="7" href="/episodes/filter/7">7</DropdownItem>
          <DropdownItem key="8" href="/episodes/filter/8">8 </DropdownItem>
        </DropdownMenu>
      </Dropdown>
    </div>
  );
}
