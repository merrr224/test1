package order.bizlogic.exception;

import java.util.ArrayList;
import java.util.List;

/**
 * 
 * 
 * @author 
 *
 */
public class FailOrderRegistrationException extends AppException {

	/** serialVersionUID */
	private static final long serialVersionUID = 1L;
	
	/** 受注登録時に既に削除されていた商品コードのリスト */
	private List<String> deletedProductList;
	
	/** 受注登録時に販売終了となっていた商品コードのリスト */
	private List<String> saleEndProductList;
	
	/**
	 * コンストラクタ
	 */
	public FailOrderRegistrationException() {
		super();
	}
	
	/**
	 * コンストラクタ
	 * 
	 * @param message 詳細メッセージ
	 * @see Exception#Exception(String)
	 */
	public FailOrderRegistrationException(String message) {
		super(message);
	}
	
	/**
	 * コンストラクタ
	 * 
	 * @param cause この例外クラスのインスタンスを生成する原因となったエラー
	 * @see Exception#Exception(Throwable)
	 */
	public FailOrderRegistrationException(Throwable cause) {
		super(cause);
	}
	
	/**
	 * コンストラクタ
	 * 
	 * @param message 詳細メッセージ
	 * @param cause この例外クラスのインスタンスを生成する原因となったエラー
	 * @see Exception#Exception(String, Throwable)
	 */
	public FailOrderRegistrationException(String message, Throwable cause) {
		super(message, cause);
	}

	/**
	 * コンストラクタ
	 * 
	 * @param message 詳細メッセージ
	 * @param cause この例外クラスのインスタンスを生成する原因となったエラー
	 * @param delProdList 受注登録時に既に削除されていた商品コードのリスト
	 * @param saleEndProdList 受注登録時に既に販売終了となっていた商品コードのリスト
	 * @see Exception#Exception(String, Throwable)
	 */
	public FailOrderRegistrationException(String message, Throwable cause,
					List<String> delProdList, List<String> saleEndProdList) {
		super(message, cause);
		
		this.deletedProductList = new ArrayList<>();
		for(String prodCode: delProdList) {
			this.deletedProductList.add(prodCode);
		}

		this.saleEndProductList = new ArrayList<>();
		for(String prodCode: saleEndProdList) {
			this.saleEndProductList.add(prodCode);
		}
	}

	
	public List<String> getDeletedProductList() {
		return deletedProductList;
	}
	public void setDeletedProductList(List<String> deletedProductList) {
		this.deletedProductList = deletedProductList;
	}

	public List<String> getSaleEndProductList() {
		return saleEndProductList;
	}
	public void setSaleEndProductList(List<String> saleEndProductList) {
		this.saleEndProductList = saleEndProductList;
	}

}
