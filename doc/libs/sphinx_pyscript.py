from sphinx.application import Sphinx
from sphinx.util.docutils import nodes
from sphinx.directives import SphinxDirective


class pyscript_env(nodes.Structural, nodes.Element):
    pass


class pyscript_repl(nodes.Structural, nodes.Element):
    pass


class PyscriptEnv(SphinxDirective):
    has_content = True

    def run(self):  # noqa: D102
        node = pyscript_env()
        node.attributes = self.options
        node.content = "\n".join(self.content or [])
        return [
            node,
        ]


class PyscriptRepl(SphinxDirective):
    has_content = True

    def run(self):  # noqa: D102
        node = pyscript_repl()
        node.attributes = self.options
        node.content = "\n".join(self.content or [])
        return [
            node,
        ]


def not_write(self, node):
    """visit/depart function for declare "no write"."""
    pass


def visit_pyscript_repl(self, node: pyscript_repl):
    content = f"""
      <div style="display: grid; grid-template-columns: 2fr 1fr;">
        <py-repl
          id="sphinx-pyscript-repl-input"
          output="sphinx-pyscript-repl-output"
        >
{node.content}
        </py-repl>
        <div
          id="sphinx-pyscript-repl-output"
          class="sphinx-pyscript-repl-output"
        >
        </div>
      </div>
    """
    self.body.append(content)


def depart_pyscript_repl(self, node: pyscript_repl):
    pass


def set_using_pyscript(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict,
    doctree: nodes.document,
):
    if not doctree:
        return
    pyscript_envs = [node for node in doctree.traverse(pyscript_env)]
    if not pyscript_envs:
        return
    context["css_files"].insert(0, "https://pyscript.net/alpha/pyscript.css")
    context["css_files"].append("_static/css/pyscript-repl.css")
    metatags = context.get("metatags", "")
    metatags += f"""
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <py-env>
    {pyscript_envs[0].content}
    </py-env>
    """
    context["metatags"] = metatags


def setup(app: Sphinx):
    app.add_directive("pyscript-env", PyscriptEnv)
    app.add_directive("pyscript-repl", PyscriptRepl)
    app.add_node(
        pyscript_env,
        html=(not_write, not_write),
        latex=(not_write, not_write),
        text=(not_write, not_write),
        man=(not_write, not_write),
        texinfo=(not_write, not_write),
        revealjs=(not_write, not_write),
        dirrevealjs=(not_write, not_write),
    )
    app.add_node(
        pyscript_repl,
        html=(visit_pyscript_repl, depart_pyscript_repl),
        latex=(not_write, not_write),
        text=(not_write, not_write),
        man=(not_write, not_write),
        texinfo=(not_write, not_write),
        revealjs=(not_write, not_write),
        dirrevealjs=(not_write, not_write),
    )
    app.connect("html-page-context", set_using_pyscript)
    return {
        "version": "0.4.0",
        "env_version": 1,
        "parallel_read_safe": False,
    }
