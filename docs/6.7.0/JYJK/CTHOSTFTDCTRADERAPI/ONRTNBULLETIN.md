<p>交易所公告通知，无Req属于公有流回报</p>
<span class="anchor" id="cadf7448-2ac5-4236-a3b7-b97283518c77"></span>
## 1.函数原型
<p>virtual void OnRtnBulletin(CThostFtdcBulletinField *pBulletin) {};</p>
<span class="anchor" id="b3480c0f-2f95-419e-b820-47b7980e2912"></span>
## 2.参数
<p>pBulletin：交易所公告</p>
<pre><code>struct CThostFtdcBulletinField
{
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///交易日
    TThostFtdcDateType TradingDay;
    ///公告编号
    TThostFtdcBulletinIDType BulletinID;
    ///序列号
    TThostFtdcSequenceNoType SequenceNo;
    ///公告类型
    TThostFtdcNewsTypeType NewsType;
    ///紧急程度
    TThostFtdcNewsUrgencyType NewsUrgency;
    ///发送时间
    TThostFtdcTimeType SendTime;
    ///消息摘要
    TThostFtdcAbstractType Abstract;
    ///消息来源
    TThostFtdcComeFromType ComeFrom;
    ///消息正文
    TThostFtdcContentType Content;
    ///WEB地址
    TThostFtdcURLLinkType URLLink;
    ///市场代码
    TThostFtdcMarketIDType MarketID;
};
</code></pre>
<span class="anchor" id="ce1a1fc0-f26a-487f-9cba-b3ebf8599c72"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ea9293e7-eb97-491d-aff1-b48bfe20c145"></span>
## 4.FAQ
<p>无</p>
