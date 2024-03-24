<p>取消订阅询价应答，当<a href="../../CTHOSTFTDCMDAPI/UNSUBSCRIBEFORQUOTERSP/">UnSubscribeForQuoteRsp</a>后，调用此接口。</p>
<span class="anchor" id="ec4104fc-f687-441c-8699-a0ac49e2c020"></span>
## 1.函数原型
<p>virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7004c655-7c07-4cb8-8acc-9c2bf272c79e"></span>
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
<span class="anchor" id="4e180f24-2772-4206-827a-381f0115cee4"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="23dc4373-e096-460b-956f-50118aa6135e"></span>
## 4.FAQ
<p>无</p>
