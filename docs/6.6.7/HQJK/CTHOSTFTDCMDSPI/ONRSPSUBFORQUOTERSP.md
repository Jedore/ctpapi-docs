<p>订阅询价应答，当调用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEFORQUOTERSP/">SubscribeForQuoteRsp</a>后，通过此接口返回。</p>
<span class="anchor" id="19e4a0f9-d491-4975-92ae-9288e84d79ae"></span>
## 1.函数原型
<p>virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="9ec5e7e9-ee62-43fe-8983-10c27b24257e"></span>
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
<span class="anchor" id="abb2044a-1db3-4a76-bb55-3197080201d6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="11830801-0ab7-4528-b422-2b8874cda5dc"></span>
## 4.FAQ
<p>无</p>
