<p>交易所公告通知，无Req属于公有流回报</p>
<span class="anchor" id="eb4fa129-c2d5-4aa9-a2d6-daaeac5ac7f7"></span>
## 1.函数原型
<p>virtual void OnRtnBulletin(CThostFtdcBulletinField *pBulletin) {};</p>
<span class="anchor" id="c175d574-ee8a-47f5-af91-dfef7d65d4cb"></span>
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
<span class="anchor" id="2097326b-d12d-42c3-bfb5-29b84dc6f714"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="627a5988-c0c7-4981-ac4d-fdb445386b59"></span>
## 4.FAQ
<p>无</p>
