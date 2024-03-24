<p>交易通知，无Req属于私有流回报。</p>
<span class="anchor" id="f7b06426-0b8d-4bad-82ab-49a5db62c09d"></span>
## 1.函数原型
<p>virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {};</p>
<span class="anchor" id="57ee6cc2-1e09-4ef1-b9d3-3260fb98db04"></span>
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
<span class="anchor" id="96e21169-e9e0-4d8c-a797-7a16426773ac"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4c7b102e-293f-45da-9ea9-84981b3dad3d"></span>
## 4.FAQ
<p>无</p>
