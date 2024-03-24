<p>删除预埋撤单响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQREMOVEPARKEDORDERACTION/">ReqRemoveParkedOrderAction</a>后，该方法被调用。</p>
<span class="anchor" id="fa62bf5c-ba0e-461b-9ba7-a52ae3111c7e"></span>
## 1.函数原型
<p>virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="4450da4b-36bc-47b5-b970-7544bc342cf7"></span>
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
<span class="anchor" id="9ee4435f-5b3c-4e10-b503-c7991f695d9e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="03805803-34e1-4b4e-8e88-aa81a4cf9183"></span>
## 4.FAQ
<p>无</p>
