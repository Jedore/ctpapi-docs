<p>请求SPBM组合保证金套餐查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTERPARAMETER/">ReqQrySPBMInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="514174f8-f3ae-4471-867b-60c10e29a5da"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMPortfDefinition(CThostFtdcSPBMPortfDefinitionField *pSPBMPortfDefinition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="173cca86-60cb-4c93-8cf9-123e481ab8e5"></span>
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
<span class="anchor" id="881fd08d-9a1e-4d49-98f1-0c94c175116c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2c02e1d4-c9d4-4afc-8959-806116d88fac"></span>
## 4.FAQ
<p>无</p>
