<p>删除预埋撤单响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQREMOVEPARKEDORDERACTION/">ReqRemoveParkedOrderAction</a>后，该方法被调用。</p>
<span class="anchor" id="29255915-b364-4ae7-a350-2ca9db1467d6"></span>
## 1.函数原型
<p>virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="da83fd50-879c-415b-a0a8-a0cb0fe97a57"></span>
## 2.参数
<p>pRemoveParkedOrderAction：删除预埋撤单</p>
<pre><code>struct CThostFtdcRemoveParkedOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///预埋撤单编号
    TThostFtdcParkedOrderActionIDType ParkedOrderActionID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="fefd3c37-4122-43c1-b140-4d6e79beb5cd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9354aa87-5d07-4ecc-96a8-a5278c590623"></span>
## 4.FAQ
<p>无</p>
