<p>交易通知，无Req属于私有流回报。</p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p>注：风控终端发送的风险通知由此接口接收。</p>
<span class="anchor" id="30ec12c1-6636-4ab4-b62a-74e2f7e7d099"></span>
## 1.函数原型
<p>virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {};</p>
<span class="anchor" id="04d7a185-c6bf-4413-80c4-49584683d2b0"></span>
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
<span class="anchor" id="60509e91-f521-4b66-8374-13234ff94b6f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6c06fa49-288c-41b6-a044-31c73374f5a3"></span>
## 4.FAQ
<p>无</p>
