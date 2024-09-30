<p>交易通知，无Req属于私有流回报。</p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p>注：风控终端发送的风险通知由此接口接收。</p>
<span class="anchor" id="57a99c9f-fedd-4b11-8a11-b07630c28acf"></span>
## 1.函数原型
<p>virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {};</p>
<span class="anchor" id="aa511342-e165-4866-989e-02f041609487"></span>
## 2.参数
<p>pTradingNoticeInfo：用户事件通知信息</p>
<pre><code>struct CThostFtdcTradingNoticeInfoField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///发送时间
    TThostFtdcTimeType SendTime;
    ///消息正文
    TThostFtdcContentType FieldContent;
    ///序列系列号
    TThostFtdcSequenceSeriesType SequenceSeries;
    ///序列号
    TThostFtdcSequenceNoType SequenceNo;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<span class="anchor" id="8140022b-7e4b-43f9-b9b3-379b8b0bd453"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0b8aff7c-b5c0-44de-b948-e13e6635f691"></span>
## 4.FAQ
<p>无</p>
