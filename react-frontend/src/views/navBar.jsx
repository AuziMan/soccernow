import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

function headerNavBar() {
  return (
    <Navbar expand="lg" className="bg-body-tertiary justify-content-center">
  <Container>
    <Navbar.Brand href="/">Soccer Now</Navbar.Brand>
    <Navbar.Toggle aria-controls="basic-navbar-nav" />
    <Navbar.Collapse id="basic-navbar-nav" className="justify-content-center">
      <Nav className="mx-auto">
        <Nav.Link href="/live-games" className="mx-3">Live Games</Nav.Link>
      </Nav>
        <Nav className="ml-auto"> {/* Push this dropdown to the right */}
          <NavDropdown title="Leagues" id="basic-nav-dropdown" className="mx-3">
            <NavDropdown.Item href="/leagues/253">MLS</NavDropdown.Item>
            <NavDropdown.Item href="/leagues/255">USL</NavDropdown.Item>
            <NavDropdown.Item href="/leagues/39">EPL</NavDropdown.Item>
            <NavDropdown.Item href="/leagues/2">UCL</NavDropdown.Item>
          </NavDropdown>
        </Nav>
    </Navbar.Collapse>
  </Container>
</Navbar>
  );
}

export default headerNavBar;