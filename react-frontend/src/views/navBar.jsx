import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

function headerNavBar() {
  return (
    <Navbar expand="lg" className="bg-body-tertiary justify-content-center">
  <Container>
    <Navbar.Brand href="#home">Soccer Now</Navbar.Brand>
    <Navbar.Toggle aria-controls="basic-navbar-nav" />
    <Navbar.Collapse id="basic-navbar-nav" className="justify-content-center">
      <Nav>
        <Nav.Link href="#home">Home</Nav.Link>
        <Nav.Link href="#link">Live Games</Nav.Link>
        <NavDropdown title="Leagues" id="basic-nav-dropdown">
          <NavDropdown.Item href="/leagues/253">MLS</NavDropdown.Item>
          <NavDropdown.Item href="/leagues/255">USL</NavDropdown.Item>
          <NavDropdown.Item href="/leagues/39">EPL</NavDropdown.Item>
        </NavDropdown>
      </Nav>
    </Navbar.Collapse>
  </Container>
</Navbar>
  );
}

export default headerNavBar;