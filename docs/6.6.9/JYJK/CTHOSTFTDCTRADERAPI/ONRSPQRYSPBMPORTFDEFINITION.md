<p>请求SPBM组合保证金套餐查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTERPARAMETER/">ReqQrySPBMInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="1d40175b-8418-4065-b4fe-ef37f30db7f9"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMPortfDefinition(CThostFtdcSPBMPortfDefinitionField *pSPBMPortfDefinition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6e687b5a-7d2b-427a-9c60-35a9c18c37be"></span>
## 2.参数
<p>pSPBMPortfDefinition：组合保证金套餐</p>
<pre><code>struct CThostFtdcSPBMPortfDefinitionField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///组合保证金套餐代码
    TThostFtdcPortfolioDefIDType    PortfolioDefID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
    ///是否启用SPBM
    TThostFtdcBoolType  IsSPBM;
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
<span class="anchor" id="d07c896f-e58a-4454-92e6-91fe528fa5c4"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6d443be0-f8e8-4828-990d-cee4ecb211cf"></span>
## 4.FAQ
<p>无</p>
