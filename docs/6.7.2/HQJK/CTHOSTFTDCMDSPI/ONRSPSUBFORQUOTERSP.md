<p>订阅询价应答，当调用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEFORQUOTERSP/">SubscribeForQuoteRsp</a>后，通过此接口返回。</p>
<span class="anchor" id="c7b30fce-84f6-46ab-b088-ef8208a61098"></span>
## 1.函数原型
<p>virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5ff60f93-dd1a-41f1-b77a-5a27ff41294d"></span>
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
<span class="anchor" id="19141aae-831b-440e-aae5-3c07d6fa33c8"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8b0531d8-a80d-492c-b7dd-eac6645e53c3"></span>
## 4.FAQ
<p>无</p>
