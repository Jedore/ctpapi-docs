<p>请求SPBM期权合约参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMOPTIONPARAMETER/">OnRspQrySPBMOptionParameter</a></p>
<span class="anchor" id="1fb63634-d47e-4192-be52-6d12d6edb892"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMOptionParameter(CThostFtdcQrySPBMOptionParameterField *pQrySPBMOptionParameter, int nRequestID) = 0;</p>
<span class="anchor" id="42207825-1910-475c-8364-19ad4ad09765"></span>
## 2.参数
<p>pQrySPBMOptionParameter：SPBM期权合约保证金参数查询</p>
<pre><code>struct CThostFtdcQrySPBMOptionParameterField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
};
</code></pre>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">品种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="cb7769ed-cacf-44c7-a744-435ae14ba30f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c1894890-cb43-4a9d-80cf-1752dce74057"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="92129383-69f6-4114-a78a-9b21e589afb7"></span>
## 5.FAQ
<p>无</p>
