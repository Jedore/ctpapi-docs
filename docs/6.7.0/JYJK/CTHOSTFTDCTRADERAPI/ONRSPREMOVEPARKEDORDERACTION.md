<p>删除预埋撤单响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQREMOVEPARKEDORDERACTION/">ReqRemoveParkedOrderAction</a>后，该方法被调用。</p>
<span class="anchor" id="4a5007d1-30f5-432b-9c7f-243c97179e4a"></span>
## 1.函数原型
<p>virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f4d6f288-8875-40ff-b8c6-f1fe92e0ee57"></span>
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
<span class="anchor" id="709bd769-33aa-4e67-8974-120dca61a985"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="31c0f5f2-a6bc-4abc-bfc9-17167ff76093"></span>
## 4.FAQ
<p>无</p>
