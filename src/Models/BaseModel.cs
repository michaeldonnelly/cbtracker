using System;
namespace ComicBookTracker.Models
{
    public partial class BaseModel
    {
        public BaseModel()
        {
        }

        public DateTime Updated { get; set; }
        public DateTime Created { get; set; }

        public void TimeStampCreate()
        {
            Created = DateTime.Now;
            Updated = Created;
        }

        public void TimeStampUpdate()
        {
            Updated = DateTime.Now;
        }
    }
}
