using System;
using System.Threading.Tasks;
using ComicBookTracker.Models;
using Microsoft.AspNetCore.Mvc;

namespace ComicBookTracker.Controllers
{
    public abstract class BaseController : Controller
    {
        protected readonly ComicBookTrackerContext _context;

        public BaseController(ComicBookTrackerContext context)
        {
            _context = context;
        }
    }
}
