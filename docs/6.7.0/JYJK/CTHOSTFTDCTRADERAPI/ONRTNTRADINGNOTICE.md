<p>交易通知，无Req属于私有流回报。</p>
<span class="anchor" id="a4c23c04-c5bb-4f42-814c-0ba8f549c310"></span>
## 1.函数原型
<p>virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {};</p>
<span class="anchor" id="b8491ee4-c885-4f0d-aca6-c2567cb08005"></span>
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
<span class="anchor" id="e8650b1f-bb29-4da5-b57f-00dea3df17e9"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5e200368-cfee-4158-8018-c4fd79cea551"></span>
## 4.FAQ
<p>无</p>
