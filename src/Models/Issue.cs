using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;

#nullable disable

namespace ComicBookTracker.Models
{
    [Table("cbtracker_issue")]
    public partial class Issue
    {
        public Issue()
        {
            Tags = new HashSet<Tag>();
        }

        public long Id { get; set; }

        [Column("issue_number")]
        public long IssueNumber { get; set; }

        public bool Own { get; set; }

        [Column("release_day")]
        public int ReleaseDay { get; set; }

        [Column("release_month")]
        public int? ReleaseMonth { get; set; }

        [Column("release_year")]
        public int? ReleaseYear { get; set; }

        public string ReleaseDateString(bool sortable = false)
        {
            string dateFormat;
            int month = (int)ReleaseMonth;
            int day = ReleaseDay;
            
            if (!ReleaseYear.HasValue)
            {
                return "";
            }
            else if (month == 0)
            {
                month = 1;
                day = 1;
                dateFormat = "yyyy";
            }
            else if (day == 0)
            {
                day = 1;
                dateFormat = "MMM yyyy";
            }
            else
            {
                dateFormat = "MMM dd yyyy";
            }

            if (sortable)
            {
                dateFormat = "yyyy-MM-dd";
            }

            DateTime releaseDate = new DateTime((int)ReleaseYear, month, day);
            return releaseDate.ToString(dateFormat);
        }

        public DateTime ReleaseDate()
        {
            return new DateTime((int)ReleaseYear, (int)ReleaseMonth, ReleaseDay);
        }

        public string Variant { get; set; }

        [Column("story_name")]
        public string StoryName { get; set; }

        [Column("story_part")]
        public long? StoryPart { get; set; }

        public string Story()
        {
            string story = StoryName;
            if (StoryPart.HasValue)
            {
                story += " " + StoryPart.ToString();
            }
            return story;
        }

        [Column("fair_price")]
        public decimal? FairPrice { get; set; }

        [Column("price_source")]
        public string PriceSource { get; set; }
        public DateTime Updated { get; set; }
        public DateTime Created { get; set; }

        [Column("author_id")]
        public long? AuthorId { get; set; }

        [Column("publisher_id")]
        public long? PublisherId { get; set; }

        [Column("series_id")]
        public long SeriesId { get; set; }

        [Column("cover_month")]
        public long? CoverMonth { get; set; }

        [Column("cover_year")]
        public long? CoverYear { get; set; }
        public bool Ordered { get; set; }
        public bool Want { get; set; }
        public bool Annual { get; set; }

        [Column("reading_order")]
        public long? ReadingOrder { get; set; }
        public bool Special { get; set; }
        public bool PullList { get; set; }

        [Column("might_own")]
        public bool MightOwn { get; set; }

        [Column("magazine_size")]
        public bool MagazineSize { get; set; }


        public virtual Author Author { get; set; }
        public virtual Publisher Publisher { get; set; }
        public virtual Series Series { get; set; }
        public virtual ICollection<IssueTag> IssueTags { get; set; }
        public virtual ICollection<Tag> Tags { get; set; }

        public override string ToString()
        {
            string name;
            if (Annual)
            {
                name = String.Format("{0} Annual #{1} ({2})", Series.ToString(), IssueNumber.ToString(), CoverYear.ToString());
            }
            else if (Special)
            {
                name = String.Format("{0} Special: {1} (#{2})", Series.ToString(), StoryName, IssueNumber.ToString());
            }
            else
            {
                name = String.Format("{0} #{1}", Series.ToString(), IssueNumber.ToString());
            }

            return name;
        }

        public string Sortable()
        {
            string extra = "";
            if (Annual)
            {
                extra = "A";
            }
            else if (Special)
            {
                extra = "S";
            }

            string issue = IssueNumber.ToString("D4");
            return string.Format("{0}-{1}{2}-{3}", Series.Sortable(), extra, issue, CoverYear);
        }
    }
}
