<p>取消订阅询价应答，当<a href="../../CTHOSTFTDCMDAPI/UNSUBSCRIBEFORQUOTERSP/">UnSubscribeForQuoteRsp</a>后，调用此接口。</p>
<span class="anchor" id="0919d66f-fbad-4fa0-b463-a251b6f03148"></span>
## 1.函数原型
<p>virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="18f74759-794e-4748-99f9-2854a38f4e8d"></span>
## 2.参数
<p>pSpecificInstrument：指定的合约</p>
<pre><code>struct CThostFtdcSpecificInstrumentField
{
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
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
<span class="anchor" id="d8260521-ba66-429b-921f-a77e35444840"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d60c7428-87ba-4abf-862b-b8fd9c568d65"></span>
## 4.FAQ
<p>无</p>
